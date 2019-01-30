import matplotlib.pyplot as plt
t = np.arange(-3,3,.01)
s = np.exp(-(t*t) + 10j * t)
plt.plot(t, s.real, 'b-', t, s.imag, 'r--', t, s * s.conjugate(), 'g')
plt.legend(('real', 'imaginary','total'))
plt.show()
