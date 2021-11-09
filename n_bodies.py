#!/usr/bin/env python
import math 

class Particle():
    """
    In this class we define our particles to use in a
    M bodies model, each one has a mass(m), a position(p)
    and a velocity(v).
    """
    m = 1.0 
    p = [0.0, 0.0, 0.0] 
    v = [0.0, 0.0, 0.0] 
    
    def __init__(self, m, p, v):
        # m: float, mass of the particle (kg)
        # p: float list, position of the particle (m)
        # v: float list, velocity of the particle (m/s)
        self.m = m
        self.p = p
        self.v = v
        
    def print_position(self, time=0):
        """
        Function to print the position of the
        particle at some especific time.
        """
        print(time, self.p)

    def __sub__(self, other):
        """
        Overload the operator "-", in this case we
        can only do a vector substract between two 
        particles's position
        """
        v1 = self.p
        v2 = other.p
        return [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]


    
class Container():
    """
    This class describes a set of particles and the
    time that passes.
    """
    particles = []
    
    def __init__(self, particles, time = 0.0):
        # particles: list of object Particle
        # time: integer that represents the time
        self.particles = particles
        self.time = time

    def print_position(self):
        """
        Prints the time and position of each
        particle inside the container.
        """
        for p in self.particles:
            p.print_position(self.time)


class Integrator():
    """
    As it's name says, this class helps us to
    integrate
    """
    t0 = 0.0
    dt = 1 
    steps = 1 
    M = 0

    def __init__(self, t0, dt, steps, M):
        # t0: float, represents the initial time
        # dt: float, represents the change in time
        # steps: int, number of iterations
        # M: int, number of particles
        self.t0 = t0
        self.dt = dt
        self.steps = steps
        self.M = M
    
    def trapeze(self, container):
        self.t0 += self.dt
        container.time = self.t0 
        G = 6.67*pow(10,-11)

        for i in range(self.M):
            
            p_i = container.particles[i]
            for j in range(self.M):
                p_j = container.particles[j]
                
                u = p_j - p_i
                ux = u[0]
                uy = u[1]
                uz = u[2]

                r = math.sqrt(ux**2 + uy**2 + uz**2)
                C = (G*p_i.m*p_j.m)/pow(r,3) if r!=0 else 0

                Fx = C*ux
                Fy = C*uy
                Fz = C*uz

        return container


    def get_t(self):
        """
        Function to get the time
        """
        return self.t0

        
M = 2 #number of particles
N = 10 #number of iterations

p0 = Particle(1, [0,0,0], [0,0,0])
p1 = Particle(1, [1,0,0], [0,0,0])


c1 = Container([p0,p1])

s1 = Integrator(0.0, 0.1, 1, M)

print(M,N)

for i in range(N):
    c1 = s1.trapeze(c1)
    c1.print_position()