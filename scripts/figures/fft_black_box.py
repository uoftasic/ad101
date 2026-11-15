"""The FFT as a machine: time waveform in, spectrum (amplitudes vs frequency) out."""
import schemdraw.flow as flow

from circuit_style import drawing, save

d = drawing()
d.add(flow.Arrow().right(3.4).label("time waveform", loc="top", ofst=0.12))
fft = d.add(flow.Box(w=1.8, h=1.1).anchor("W").label("FFT"))
d.add(flow.Arrow().right(5.4).at(fft.E).label("spectrum\n(amplitudes vs frequency)", loc="top", ofst=0.12))
print(save(d, "ad101-fft-black-box"))
