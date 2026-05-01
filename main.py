import os
import yaml
import time
import random
import re
from atproto import Client, models
from google import genai

# --- UTILITY: FACET PARSER ---
def parse_facets(text):
    facets = []
    # Detect URLs
    url_regex = r'(https?://[^\s/$.?#].[^\s]*)'
    for match in re.finditer(url_regex, text):
        start, end = match.start(), match.end()
        url = match.group()
        facets.append(models.AppBskyRichtextFacet.Main(
            features=[models.AppBskyRichtextFacet.Link(uri=url)],
            index=models.AppBskyRichtextFacet.ByteSlice(
                byte_start=len(text[:start].encode('utf-8')),
                byte_end=len(text[:end].encode('utf-8'))
            )
        ))
    # Detect Hashtags
    hashtag_regex = r'#(\w+)'
    for match in re.finditer(hashtag_regex, text):
        start, end = match.start(), match.end()
        tag = match.group(1)
        facets.append(models.AppBskyRichtextFacet.Main(
            features=[models.AppBskyRichtextFacet.Tag(tag=tag)],
            index=models.AppBskyRichtextFacet.ByteSlice(
                byte_start=len(text[:start].encode('utf-8')),
                byte_end=len(text[:end].encode('utf-8'))
            )
        ))
    return facets

# --- CONFIG LOADING ---
def load_config():
    try:
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ [CONFIG] Error: {e}")
        raise

# --- AI GENERATION ---
def get_ai_content(client_ai, prompt, persona):
    model_name = "gemini-2.5-flash"
    full_prompt = prompt.format(persona=persona)
    try:
        print(f"🤖 [AI] Generating content with {model_name}...")
        response = client_ai.models.generate_content(model=model_name, contents=full_prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ [AI] Error: {e}")
        return None

# --- MAIN RUNNER ---
def run_bot():
    print("🚀 [START] Post-Only Broadcast Mode")
    config = load_config()
    daily = config['daily_post']
    identity = config['bot_identity']
    
    # Authentication
    try:
        client_ai = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        client_bsky = Client()
        client_bsky.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_PASSWORD"])
        print("✅ [AUTH] Connected to BlueSky & Gemini.")
    except Exception as e:
        print(f"❌ [AUTH] Login failed: {e}")
        return

    # Post Logic
    if daily['enabled']:
        # Random topic selection
        selected_topic = random.choice(daily['topic_pool'])
        
        # Pre-post delay for realism
        wait_time = random.randint(*daily['pre_post_delay'])
        print(f"⏳ [WAIT] Waiting {wait_time}s before posting about: {selected_topic}")
        time.sleep(wait_time)

        # Generate text
        raw_text = get_ai_content(
            client_ai, 
            daily['post_prompt'].format(topic=selected_topic, persona=identity['persona']),
            identity['persona']
        )

        if raw_text:
            final_text = raw_text[:280] # Safety truncate
            try:
                print(f"📤 [POST] Sending: {final_text[:50]}...")
                client_bsky.send_post(
                    text=final_text,
                    facets=parse_facets(final_text)
                )
                print("✅ [SUCCESS] Content is live.")
            except Exception as e:
                print(f"❌ [ERROR] Broadcast failed: {e}")

    print("👋 [EXIT] Run complete.")

if __name__ == "__main__":
    run_bot()
