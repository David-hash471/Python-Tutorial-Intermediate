import configparser, random, string, sys
from pathlib import Path
CONFIG_FILE = Path(__file__).with_name('config.ini')

def read_config_option():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    setting = {section: dict(config.items(section)) for section in config.sections()}
    return config
    
    
    
    

def generate_password(length, uppercase, digits, special):
    character = string.ascii_lowercase
    if uppercase:
        character += string.ascii_uppercase
    if digits:
        character += string.digits
    if special:
        character += string.punctuation
    return ''.join(random.choice(character) for _ in range(int(length)))

def main():
    if len(sys.argv) == 5:
        password = generate_password(
            int(sys.argv[1]),
            bool(sys.argv[2]),
            bool(sys.argv[3]),
            bool(sys.argv[4]),

        )   
    else:
        config = read_config_option()
        password = generate_password(
            config.getint('Length', 'password_length'), 
            config.getboolean('CharTypes', 'uppercase'), 
            config.getboolean('CharTypes', 'digits'), 
            config.getboolean('CharTypes', 'special')
        )
        
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()