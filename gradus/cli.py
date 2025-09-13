import argparse
from .hist_embed import encode
from .hist_extract import decode


def main():
    parser = argparse.ArgumentParser(description='Image steganography tool using histogram shifting method.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    ### Embed commands
    embed = subparsers.add_parser('embed', help='Hide text in an image')
    embed.add_argument('--in', dest='payload', required=True, help='Write the text to hide')
    embed.add_argument('--cover', dest='image', required=True, help='cover audio')
    embed.add_argument('--key', required=True, help='Enter the key for encryption and randomization pixels')

    ### Extract commands
    extract = subparsers.add_parser('extract',help='Extract the hidden payload')
    extract.add_argument('--stego', required=True, help='Image with hidden payload')
    extract.add_argument('--key', required=True, help='Enter the key used for embedding')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        exit(1)

    try:
        if args.command == 'embed':
            encode(args.image, args.payload, args.key)
            print("Successfully embedded the payload in the encoded.png")
        elif args.command == 'extract':
            decode(args.stego, args.key)
            print("Successfully extracted the payload")
    except Exception as e:
        print(f"Error : {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()