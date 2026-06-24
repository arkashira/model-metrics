import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

@dataclass
class BenchmarkSuite:
    id: str
    results: dict

class ModelMetrics:
    def __init__(self):
        self.suites = {}
        self.tokens = {}

    def create_suite(self, results):
        suite_id = str(uuid4())
        self.suites[suite_id] = BenchmarkSuite(suite_id, results)
        return suite_id

    def generate_share_link(self, suite_id):
        token = str(uuid4())
        self.tokens[token] = suite_id
        return f"https://example.com/{suite_id}/{token}"

    def get_results(self, suite_id, token):
        if token not in self.tokens or self.tokens[token] != suite_id:
            raise ValueError("Invalid token")
        if suite_id not in self.suites:
            raise ValueError("Suite not found")
        return self.suites[suite_id].results

    def revoke_link(self, suite_id, token):
        if token not in self.tokens or self.tokens[token] != suite_id:
            raise ValueError("Invalid token")
        del self.tokens[token]
