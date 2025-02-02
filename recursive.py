import time

def tower_of_hanoi_recursive(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi_recursive(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi_recursive(n - 1, auxiliary, destination, source)

n = int(input("Jumlah n (minimal 3) : "))
if n < 3 : n = 3
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")