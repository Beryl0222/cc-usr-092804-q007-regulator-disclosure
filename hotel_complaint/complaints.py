"""住宿价格争议与证据版本。"""
from dataclasses import dataclass
@dataclass
class Evidence: evidence_id: str; order_id: str; price: int; captured_at: str; status: str = 'open'
class ComplaintBook:
    def __init__(self): self.evidence = {}; self.orders = {}
    def submit(self, evidence): self.evidence[evidence.evidence_id] = evidence; self.orders.setdefault(evidence.order_id, []).append(evidence.evidence_id)
    def close(self, order_id, refund): self.orders[order_id] = {'state': 'closed', 'refund': refund}
    def timeline(self, order_id):
        ids = self.orders.get(order_id, [])
        if isinstance(ids, dict): return [ids]
        return [self.evidence[i].__dict__ for i in ids]
    def reopen(self, order_id):
        if isinstance(self.orders.get(order_id), dict): self.orders[order_id]['state'] = 'open'
