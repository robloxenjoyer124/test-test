# NexusScan

```
    _   __                     _____can
   / | / /__  _  ____  _______/ ___/_________U__
  /  |/ / _ \| |/_/ / / / ___/\__ \/ ___/ __ `/ __ \
 / /|  /  __/>  </ /_/ (__  )___/ / /__/ /_/ / / / /
/_/ |_/\___/_/|_|\__,_/____//____/\___/\__,_/_/ /_/
```

**NexusScan** is a powerful, textured, and animated OSINT (Open Source Intelligence) tool for the CLI. It provides a sleek and modern terminal interface to gather information about IP addresses, DNS records, and usernames across various platforms.

## Features

- **IP Lookup**: Detailed geolocation, ISP, and organization information for any IP address.
- **DNS Enumeration**: Retrieve A, AAAA, MX, NS, and TXT records for any domain.
- **Username Check**: Check for the existence of a username across 10+ popular social media and coding platforms.
- **Rich UI**: Beautiful, animated, and colored output using the `rich` library.

## Installation

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nexus_scan.git
   cd nexus_scan
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package (optional):
   ```bash
   pip install .
   ```

## Usage

You can run the tool directly using `main.py` or as an installed command `nexus-scan`.

### IP Lookup

```bash
python main.py ip 8.8.8.8
# or
nexus-scan ip 8.8.8.8
```

### DNS Lookup

```bash
python main.py dns google.com
# or
nexus-scan dns google.com
```

### Username Check

```bash
python main.py user torvalds
# or
nexus-scan user torvalds
```

## License

MIT
