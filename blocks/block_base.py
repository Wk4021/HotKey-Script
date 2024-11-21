class BlockBase:
    def __init__(self, block_type, description=""):
        """
        Initialize a block with a type and optional description.
        """
        self.block_type = block_type
        self.description = description
        self.next_block = None

    def set_next_block(self, next_block):
        """
        Set the next block in the sequence.
        """
        self.next_block = next_block

    def execute(self):
        """
        Placeholder for block execution logic.
        This should be overridden by specific block types.
        """
        raise NotImplementedError("Execute method should be implemented by subclasses")

    def get_description(self):
        """
        Get the description of the block.
        """
        return self.description

    def __str__(self):
        """
        String representation of the block.
        """
        return f"Block Type: {self.block_type}, Description: {self.description}"

# Example usage of BlockBase class
if __name__ == "__main__":
    block = BlockBase("Generic Block", "This is a generic block.")
    print(block)
    try:
        block.execute()
    except NotImplementedError as e:
        print(e)
