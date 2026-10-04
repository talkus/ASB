from journal import Journal
from doctor.doctor_live import DoctorLive

def main():
    DoctorLive("local", Journal()).status()

if __name__ == "__main__":
    main()
