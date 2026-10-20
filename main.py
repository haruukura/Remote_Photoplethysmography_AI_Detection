import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np

import yarppg

filename = "SampleVideos/"
fps = yarppg.helpers.get_video_fps(filename)

rppg = yarppg.Rppg()

results: list[yarppg.RppgResult] = []

for frame in yarppg.frames_from_video(filename):
    results.append(rppg.process_frame(frame))

plt.plot(np.array(results)[:, 0])  # plot rPPG signal
