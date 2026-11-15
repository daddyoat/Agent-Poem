
from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)

poem = """A Life of My Own

I was not born to drift like leaves,
Or live inside what fate conceives.
The world may draw the lines I face,
But I decide my walking pace.

I may not choose the falling rain,
The doors that close, the roads of pain.
But I can plant where ashes lie,
And build a ladder to the sky.

One choice, one step, one brave refusal,
A thousand turns, a new arrival.
For life is more than what we inherit;
It's what we dare to do with it."""

(output_dir / "entry.txt").write_text(poem, encoding="utf-8")
