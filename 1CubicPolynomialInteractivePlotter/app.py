import streamlit as st
import numpy as np
import plotly.graph_objects as go


st.title("Cubic Polynomial - Interactive Plotter")
st.write("Adjust the Coefficients to see how the Cubic Polynomial Evolves!")

cola, colb, colc, cold = st.columns(4)
with cola:
    a = st.slider("a", -5.0, 5.0, 1.0)
with colb:
    b = st.slider("b", -10.0, 10.0, 0.0)
with colc:
    c = st.slider("c", -10.0, 10.0, 0.0)
with cold:
    d = st.slider("d", -20.0, 20.0, 0.0)

st.write("")
Eq = f"y = {a:.1f}x^3"
Eq += f" + {b:.1f}x^2" if b>= 0 else f" - {abs(b):.1f}x^2"
Eq += f" + {c:.1f}x" if c >= 0 else f" - {abs(c):.1f}x"
Eq += f" + {d:.1f}" if d >= 0 else f" - {abs(d):.1f}"

st.latex(Eq)
st.write("")

colminlim, colmaxlim = st.columns(2)
with colminlim:
    x_lower_limit = st.number_input("Lower Limit", value=-5.0, step=0.1)
with colmaxlim:
    x_upper_limit = st.number_input("Upper Limit", value=5.0, step=0.1)
st.write("")

x = np.linspace(x_lower_limit, x_upper_limit, int(np.abs(x_upper_limit - x_lower_limit)*100))
y = a*x**3 + b*x**2 + c*x + d

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Curve'))
fig.update_layout(title='Cubic Polynomial', xaxis_title='x', yaxis_title='y', showlegend=True)

show_roots = st.checkbox("Show Roots")
if show_roots:
    roots = np.roots([a, b, c, d])

    root1, root2, root3 = st.columns(3)
    with root1:
        st.latex(rf"x_1: {roots[0]:.4f}")
    with root2:
        st.latex(rf"x_2: {roots[1]:.4f}")
    with root3:
        st.latex(rf"x_3: {roots[2]:.4f}")

    real_roots = roots[np.isreal(roots)].real
    fig.add_trace(go.Scatter(x=real_roots, y=np.zeros_like(real_roots), mode='markers', name='Roots'))

st.plotly_chart(fig)