from datetime import datetime

class Logging:
    @staticmethod
    def PrintConsole(Script, Type, Msg):
        print(f"\033[{"34m" if Type == "Task" else "92m" if Type == "Success" else "0m" if Type == "Info" else "93m" if Type == "Warning" else "91m"}[{"." if Type == "Task" else "★" if Type == "Success" else "-" if Type == "Info" else "!" if Type == "Warning" else "X"}] [{datetime.now().strftime("%H:%M:%S")}] ({Script}) {Msg}")