from pathlib import Path
from datetime import datetime
from gtts import gTTS


class AudioGenerator:

    def __init__(self, output_dir="Artifacts/audio_generation"):

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_audio(self, text, language="en"):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_file = self.output_dir / f"speech_{timestamp}.mp3"

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.save(str(output_file))

        return output_file