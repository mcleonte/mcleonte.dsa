"""
https://leetcode.com/problems/odd-even-linked-list/
https://leetcode.com/problems/odd-even-linked-list/solutions/2881889/python-o-n-o-1-short-lbyl-and-eafp-examples/
https://leetcode.com/problems/odd-even-linked-list/solutions/2881668/daily-leetcoding-challenge-december-day-6/comments/1706876
"""

from typing import Optional

from .. import ListNode


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
  """
  EAFP style
  O(n) O(1)
  """
  if not head:
    return head
  odd, even, even_head = head, head.next, head.next
  while True:
    try:
      prev_odd = odd
      odd.next = odd = even.next
      even.next = even = odd.next
    except AttributeError:
      break
  odd = odd or prev_odd
  odd.next = even_head
  return head


def odd_even_list_2(head: Optional[ListNode]) -> Optional[ListNode]:
  """
  LBYL
  O(n) O(1)
  """
  if not head:
    return head
  odd, even, even_head = head, head.next, head.next
  while True:
    if not even:
      break
    prev_odd = odd
    odd.next = odd = even.next
    if not odd:
      odd = prev_odd
      break
    even.next = even = odd.next
  odd.next = even_head
  return head
