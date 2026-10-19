# bandit-check

GitHub Action for [bandit](https://github.com/PyCQA/bandit) python security linter

Make sure you have a `.bandit` file at the root of your repository!

## Inputs

### `path`

**Optional** The path to run bandit on

**Default** `"."`

**Optional** Optional Bandit flags (refer to `bandit --help`)

**Default** `""`

## Outputs

None

## Example usage

```yaml
uses: jpetrucciani/bandit-check@master

# specify a path
uses: jpetrucciani/bandit-check@master
with:
  path: '.'

# provide some flags
uses: jpetrucciani/bandit-check@master
with:
  bandit_flags: '-lll -o output.json -f json'
```

## Privacy

This Action contacts Chainguard's licensing server to verify authorization. Connection metadata (IP address, GitHub repository identifier, timestamp, and any metadata encoded in the auth token) is transmitted to Chainguard, Inc. even if authorization is denied in accordance with our [Privacy Notice](https://www.chainguard.dev/legal/privacy-notice)
