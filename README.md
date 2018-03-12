# mkjunk

Python script for generating a specific-length string of junk data. Useful for testing API length limits.

This is extremely simplistic, but unlike other "dummy text" CLI snippets, `mkjunk`:

- Does not read random characters -- output is constrained to the "seed string". Contrast with `/dev/urandom`, which can contain whitespace characters, which is sometimes annoying
- Understands human-readable lengths (e.g. `mkjunk 1mb`)
- Outputs to STDOUT instead of creating a file.
- Is probably extremely inefficient

Informational messages are written to STDERR.

## Examples

``` bash
# Write "hihi" to a file
mkjunk -s hi 4 > junk.txt

# Add 1kb of junk to a file
mkjunk 1000 >> junk.txt

# Put 1mb of junk in your clipboard (on OSX)
mkjunk 1mb | pbcopy

```

## Usage

```
Usage: mkjunk [OPTIONS] NUM_BYTES

  Accepts a NUM_BYTES (which can be human-readable, e.g. "1mb") and writes
  that many bytes of junk characters to STDOUT. The junk is just a single
  "seed string" repeated.

Options:
  -s, --seed TEXT  alternate seed text for generation
  --help           Show this message and exit.
```

Released under MIT License.