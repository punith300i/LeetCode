class Codec:
    import random
    
    hashmap = dict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            hash = ''.join([chr(random.choice(range(97,114))) for x in range(10)])
            if hash not in self.hashmap:
                self.hashmap[hash] = longUrl
                return hash


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashmap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))