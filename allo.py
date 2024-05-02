class Frame:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.allocated = False

class Fascaster:
    def __init__(self):
        self.frames = [Frame(i, 100) for i in range(10)]

    def allocate_frame(self):
        for frame in self.frames:
            if not frame.allocated:
                frame.allocated = True
                return frame
        return None

    def deallocate_frame(self, frame_id):
        for frame in self.frames:
            if frame.id == frame_id:
                frame.allocated = False
                return True
        return False

# Membuat objek fascaster
fascaster = Fascaster()

# Mengalokasikan frame
frame = fascaster.allocate_frame()
if frame:
    print(f"Frame {frame.id} dialokasikan.")
else:
    print("Tidak ada frame yang tersedia untuk dialokasikan.")

# Dealokasi frame
if fascaster.deallocate_frame(frame.id):
    print(f"Frame {frame.id} telah didealokasi.")
else:
    print("Frame tidak ditemukan.")
