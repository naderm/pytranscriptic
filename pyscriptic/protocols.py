
from pytranscriptic import runs

def submit_protocol(refs, instructions, title="PyTranscript Run"):
    request = {
        "refs": refs,
        "instructions": instructions,
        }
    runs.run(
        request,
        title=title,
        )
