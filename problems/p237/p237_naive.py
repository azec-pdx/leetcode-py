import sys

sys.path.append("..")  # allows importing everything from utils and adts

from adts.list_node import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pn = None
        cn = node
        while (nn := cn.next) is not None:
            cn.val = nn.val
            pn = cn
            cn = nn
        pn.next = None
