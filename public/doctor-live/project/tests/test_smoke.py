from core.gates import verify_gates_integrity
from doctor.doctor_live import DoctorLive
from journal import Journal


def test_gates_231():
    checks = verify_gates_integrity()
    assert checks["C22_2"] is True
    assert checks["global"] is True


def test_certificate_not_issued_without_sources():
    checks = DoctorLive("local", Journal()).check_all()
    assert checks["global"] is False
    assert checks["recu_S24"] is False
    assert checks["231_portes_C22_2"] is True
