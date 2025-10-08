from datetime import datetime

class Logging:
    Messages = []

    @staticmethod
    def PrintConsole(Script, Type, Msg):
        MsgToPush = f"\033[{"34m" if Type == "Task" else "92m" if Type == "Success" else "0m" if Type == "Info" else "93m" if Type == "Warning" else "91m"}[{"." if Type == "Task" else "★" if Type == "Success" else "-" if Type == "Info" else "!" if Type == "Warning" else "X"}] [{datetime.now().strftime("%H:%M:%S.%f")[:-3]}] ({Script}) {Msg}"
        print(MsgToPush, flush=True)
        Logging.Messages.append(MsgToPush)

    @staticmethod
    def WriteToFile(OutFile):
        print("TODO")