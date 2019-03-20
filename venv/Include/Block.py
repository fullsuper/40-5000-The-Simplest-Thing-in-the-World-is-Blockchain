import hashlib as hasher
import datetime

class Block:
  def __init__(self, index, data, previous_hash):
    self.index = index
    self.timestamp = datetime.datetime.now()
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self,index,timestamp,data,previous_hash):
    sha = hasher.sha256()
    sha.update(str(index) + str(timestamp) + str(data) + str(previous_hash))
    return sha.hexdigest()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) +
               str(self.timestamp) +
               str(self.data) +
               str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()