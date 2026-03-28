from src.engine import PayoutSentinel

def test_ind_99_fix():
    sentinel = PayoutSentinel()
    event = "Indian dev payout failed with BANKUS33"
    result = sentinel.analyze(event)
    assert "BANKUSRR" in result["result"]
    print("\nTest Passed: Correct BIC retrieved.")
