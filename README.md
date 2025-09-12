# Gradus 🔐

A steganography tool that uses histogram shifting techniques to hide encrypted text messages within PNG images. Gradus combines AES encryption with histogram-based data embedding for secure covert communication.

## 🌟 Features

- **Histogram Shifting Steganography**: Utilizes peak and zero point detection in image histograms for data embedding
- **AES Encryption**: Messages are encrypted using AES-256 in EAX mode before embedding
- **Multi-channel Distribution**: Distributes encrypted data across RGB channels
- **Key-based Security**: Uses cryptographic keys for both encryption and randomized pixel selection
- **Format Validation**: Ensures only valid PNG images are processed
- **Capacity Analysis**: Automatically calculates and reports embedding capacity
- **CLI Interface**: Simple command-line interface for embedding and extraction

## 🛠️ Quick Start

### Prerequisites

```bash
pip install Pillow numpy pycryptodome
```

### Installation

```bash
pip install gradus
```

### One-Line Installation

```bash
# System-wide (with sudo)
curl -sSL https://raw.githubusercontent.com/kaizoku73/Gradus/main/install.sh | sudo bash

# User installation (no sudo)
curl -sSL https://raw.githubusercontent.com/kaizoku73/Gradus/main/install.sh | bash
```
### Uninstallation

```bash
# To uninstall Gradus system-wide (with sudo):
curl -sSL https://raw.githubusercontent.com/kaizoku73/Gradus/main/uninstall.sh | sudo bash

# To uninstall Gradus (no sudo):
curl -sSL https://raw.githubusercontent.com/kaizoku73/Gradus/main/uninstall.sh | bash

```

### Clone Repository

```bash
git clone https://github.com/kaizoku73/Gradus.git
cd Gradus
```

## 🚀 Usage

### Embedding a Message

Hide a secret message in an image:

```bash
gradus embed --in "Your secret message here" --cover image.png --key mypassword123
```

**Parameters:**
- `--in`: The text message to hide (max 100 characters)
- `--cover`: Path to the cover PNG image
- `--key`: Password for encryption and randomization

**Output:** Creates `encoded.png` with your hidden message

### Extracting a Message

Retrieve the hidden message from a steganographic image:

```bash
gradus extract --stego encoded.png --key mypassword123
```

**Parameters:**
- `--stego`: Path to the image containing hidden data
- `--key`: The same password used during embedding

## 🔬 How It Works

### Histogram Shifting Algorithm

1. **Peak Detection**: Finds the peak (most frequent) pixel value in each RGB channel
2. **Zero Point Detection**: Identifies empty histogram bins near the peak
3. **Pixel Shifting**: Shifts pixel values between peak and zero to create embedding space
4. **Data Distribution**: Distributes encrypted payload bits across RGB channels
5. **Randomized Embedding**: Uses key-derived seeds for secure, random pixel selection

### Security Features

- **AES-256 Encryption**: Messages encrypted with AES-EAX mode before embedding
- **SHA-256 Key Derivation**: Secure key generation from passwords
- **Start/End Markers**: `HISTOSTART` and `HISTO_END!` markers for data validation
- **Randomized Selection**: Cryptographically secure pixel position randomization

## What is Histogram shift and how does it work?
For a detailed explanation of Histogram shift steganography and how it works, check out this article: https://kaizoku.gitbook.io/steganography/histogram-shift-in-image

## 🎯 Technical Specifications

- **Image Format**: PNG only (automatically validates format)
- **Color Mode**: RGB (auto-converts from other modes)
- **Message Limit**: 100 characters (padded to 100 bytes)
- **Encryption**: AES-256-EAX with nonce and authentication tag
- **Key Derivation**: SHA-256 hash of password


## 🔍 Algorithm Details

### Peak Finding Function
- Finds maximum frequency value (peak) in histogram
- Locates nearest zero-frequency bin for shifting
- Calculates embedding capacity based on peak frequency

### Bit Distribution
- Total bits distributed across 3 RGB channels
- Remainder bits allocated to first channels if not evenly divisible
- Each channel processes its allocated bit sequence

### Pixel Modification
- Peak pixels (value = u) remain unchanged for '0' bits
- Peak pixels shifted by ±1 (u + shift) for '1' bits
- Non-peak pixels shifted away to maintain histogram integrity

## ⚠️ Limitations

- Only supports PNG images (validates format before processing)
- Maximum message length: 100 characters
- Requires sufficient histogram peaks for embedding capacity
- Both embedding and extraction require identical keys
- Basic console output (no rich formatting implemented)

## 🔒 Security Considerations

- Uses AES-256-EAX providing both encryption and authentication
- Key-derived randomization prevents pattern detection
- Start/end markers ensure data integrity
- Password-based key derivation with SHA-256

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Error Handling

The tool includes comprehensive error handling for:
- Missing or invalid image files
- Non-PNG format images
- Empty or oversized messages
- Insufficient embedding capacity
- Wrong extraction keys
- Corrupted steganographic data

---

## Disclaimer

This tool is for educational and legitimate purposes only. Users are responsible for ensuring compliance with applicable laws and regulations when using steganography techniques.

---

**Made by kaizoku**