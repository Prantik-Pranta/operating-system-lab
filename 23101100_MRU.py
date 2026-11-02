# Most Recently Used (MRU) Page Replacement Algorithm
pages = list(map(int, input("Enter the page reference string: ").split()))
capacity = int(input("Enter the number of frames: "))

frames = []
page_faults = 0

print("\nPage\tFrames\t\tStatus")

for i in pages:
    if i not in frames:
        page_faults += 1

        if len(frames) < capacity:
            frames.append(i)
        else:
            frames.pop()
            frames.append(i)

        status = "Page Fault"

    else:
        frames.remove(i)
        frames.append(i)
        status = "Hit"

    print(f"{i}\t{frames}\t\t{status}")

print("\nTotal Page Faults:", page_faults)
print("Total Page Hits:", len(pages) - page_faults)