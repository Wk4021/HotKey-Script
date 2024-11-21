class ExecutionFlow:
    def __init__(self, blocks):
        # A list of blocks connected in the playground
        self.blocks = blocks
        self.execution_order = []
        self.connections = []  # Connections between blocks (e.g., from/to block references)

    def determine_flow(self):
        """
        Determine the execution order of the blocks based on how they are connected.
        """
        # Clear any previous execution order
        self.execution_order = []

        # Determine the starting block (blocks with no incoming connections)
        start_blocks = self.get_start_blocks()
        if not start_blocks:
            print("Error: No valid start block found in the flow.")
            return

        # Traverse from the start block and determine the order
        for start_block in start_blocks:
            self.traverse_blocks(start_block)

        print("Execution order determined:")
        for block in self.execution_order:
            print(f"- {block.block_type}")

    def traverse_blocks(self, block):
        """
        Recursively traverse blocks from the starting block to determine the execution order.
        """
        if block not in self.execution_order:
            self.execution_order.append(block)
        
        # Get the connected blocks that should be executed after the current block
        connected_blocks = self.get_connected_blocks(block)
        for connected_block in connected_blocks:
            self.traverse_blocks(connected_block)

    def get_start_blocks(self):
        """
        Get blocks with no incoming connections (i.e., potential starting blocks).
        """
        incoming_connections = [conn[1] for conn in self.connections]
        start_blocks = [block for block in self.blocks if block not in incoming_connections]
        return start_blocks

    def get_connected_blocks(self, block):
        """
        Get the list of blocks that are connected to the given block.
        """
        connected = [conn[1] for conn in self.connections if conn[0] == block]
        return connected

    def execute(self):
        """
        Execute the automation flow based on the determined order.
        """
        if not self.execution_order:
            print("Error: No execution order determined. Please determine the flow first.")
            return

        print("Starting execution flow:")
        for block in self.execution_order:
            block.execute()
        print("Execution flow completed.")

# Example BlockBase class to demonstrate execution
class BlockBase:
    def __init__(self, block_type):
        self.block_type = block_type

    def execute(self):
        print(f"Executing block: {self.block_type}")

if __name__ == "__main__":
    # Example usage with mock blocks
    block1 = BlockBase("Mouse Block")
    block2 = BlockBase("Keyboard Block")
    block3 = BlockBase("Wait Block")
    block4 = BlockBase("Coordinate Block")

    # Example connections
    blocks = [block1, block2, block3, block4]
    flow = ExecutionFlow(blocks)
    flow.connections = [
        (block1, block2),  # block1 -> block2
        (block2, block3),  # block2 -> block3
        (block3, block4)   # block3 -> block4
    ]

    # Determine the flow and execute
    flow.determine_flow()
    flow.execute()
