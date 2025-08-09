
class MinHeap:
	  def __init__(self):
		  self.data= []

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

	  def build_heap(self):
        # start from the last parent node and heapify down to root
        start_idx = (len(self.data) - 2) // 2
        for i in range(start_idx, -1, -1):
            self.heapify_down(i)

	  def heapify_down(self, i):
    		while True:
        	 small = i  # assume current i is smallest
       		 left = self.left_child(i)
      		 right = self.right_child(i)
       		 n = len(self.data)

        		# check if left child exists and is smaller
        		if left < n and self.data[left] < self.data[small]:
           			 small = left

        		# check if right child exists and is smaller
      		  if right < n and self.data[right] < self.data[small]:
            		small = right

       		 # if smallest is still i, heap property is restored
       			 if small == i:
           				 break

        		# swap values at i and smallest child
        		self.data[i], self.data[small] = self.data[small], self.data[i]

       		 # continue heapifying down at the new position
       		 i = small
