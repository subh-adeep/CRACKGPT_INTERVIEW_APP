# helpers/google_tts.py
from google.cloud import texttospeech
from google.oauth2 import service_account

def tts_audio_bytes(text, key_path, voice_name="en-US-Wavenet-D"):
    """
    Synthesizes speech using a specific service account key file.
    Returns the audio content in bytes.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(key_path)
        client = texttospeech.TextToSpeechClient(credentials=credentials)
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", name=voice_name
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response.audio_content
    except Exception as e:
        print(f"Google TTS Error: {e}")
        raise e