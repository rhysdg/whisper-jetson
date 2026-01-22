from whisperjet.vads.silero import Silero as Silero
from whisperjet.vads.vad import Vad as Vad

try:
    from whisperjet.vads.pyannote import Pyannote as Pyannote
except ImportError:
    Pyannote = None
