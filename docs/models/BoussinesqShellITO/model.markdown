# Boussinesq inviscid torsional oscillations in a spherical shell

The model equations are

$$
\partial_t{\bf u} + \frac{2}{Le} \hat{z}\times\{\bf u} = -\nabla p + \left(\nabla\times{\bf b}\right)\times{\bf B_0} + \left(\nabla\times{\bf B_0}\right)\times{\bf b}
$$

$$
\partial_t{\bf b} = \nabla\times\left({\bf u}\times{\bf B_0}\right) + \frac{1}{Lu}\nabla^2{\bf b}
$$

with the parameters defined as

The system is solved using a Toroidal/Poloidal decomposition of the velocity

$$
{\bf u} = \nabla\times T_u {\bf r} + \nabla\times\nabla\times P_u {\bf r} 
$$

and the magnetic field
$$
{\bf u} = \nabla\times T_b {\bf r} + \nabla\times\nabla\times P_b {\bf r} 
$$
