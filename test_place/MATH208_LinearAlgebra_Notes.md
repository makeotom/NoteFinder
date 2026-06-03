COURSE: MATH 208 - Linear Algebra
DATE: May 26, 2026
TOPIC: Vector Spaces, Subspaces, and Dimension

---

## 1. Core Definition: Vector Spaces
A Vector Space V over a scalar field R is a non-empty set of objects (vectors) equipped with two operations—vector addition (u + v) and scalar multiplication (c * u)—that satisfy the 10 structural axioms.

### The 10 Axioms (Quick Reference Checklist)
*Axioms 1–5 govern addition; 6–10 govern scalar multiplication.*
1. Closure under Addition: If u, v in V, then u + v in V.
2. Commutativity: u + v = v + u.
3. Associativity of Addition: (u + v) + w = u + (v + w).
4. Zero Vector: There exists an element 0 in V such that u + 0 = u for all u in V.
5. Additive Inverses: For every u in V, there is a -u in V such that u + (-u) = 0.
6. Closure under Scalar Mult: If u in V and c in R, then cu in V.
7. Distributivity I: c(u + v) = cu + cv.
8. Distributivity II: (c + d)u = cu + du.
9. Associativity of Scalar Mult: c(du) = (cd)u.
10. Scalar Identity: 1 * u = u.

*Common examples:* R^n, P_n (polynomials of degree <= n), M_m_n (matrices).

---

## 2. Subspaces
A subset H of a vector space V (H is a subset of V) is a subspace if it preserves the algebraic structure of V natively. Instead of checking all 10 axioms, you only need to prove 3 conditions:

1. Zero Vector Existence: The zero vector of V is in H (0 in H).
2. Closed under Addition: For any u, v in H -> u + v in H.
3. Closed under Scalar Multiplication: For any u in H and c in R -> cu in H.

> WARNING: Crucial Geometric Check
> Lines, planes, or hyperplanes in R^n are ONLY subspaces if they pass directly through the ORIGIN (0, 0, ..., 0). If a plane has a non-zero shift vector (e.g., x1 + 2x2 - x3 = 4), it is an affine set, NOT a subspace, because the zero vector fails to satisfy the equation.

---

## 3. Linear Independence, Basis, and Dimension
- Linear Independence: A set of vectors {v1, v2, ..., vk} is linearly independent if the vector equation c1*v1 + c2*v2 + ... + ck*vk = 0 has *only* the trivial solution (c1 = c2 = ... = ck = 0). If any vector can be written as a linear combination of the others, the set is dependent.
- Basis: A set B = {b1, b2, ..., bn} is a basis for a subspace H if:
    1. B is a linearly independent set.
    2. The span of B equals H (Span(B) = H).
    *Intuition:* A basis is a minimal, maximally efficient generating set for the space. No dead weight.
- Dimension (dim H): The exact number of vectors in any basis for H.
    * The dimension of the zero subspace {0} is defined to be 0.
    * The Size Rule: If dim H = n, any set in H containing more than n vectors is automatically linearly dependent. Any set with fewer than n vectors cannot span H.

---

## 4. Algorithmic Workflows for Homework Sheet 6

### Finding a Basis for the Null Space (Nul A)
Nul A = {x in R^n : Ax = 0}.
1. Set up the homogeneous system Ax = 0.
2. Row reduce A to Reduced Row Echelon Form (RREF).
3. Identify the free variables (columns without pivots).
4. Express the dependent (pivot) variables explicitly in terms of the free variables.
5. Write the general solution vector x in parametric vector form (factoring out the free variables).
6. The vectors attached to the free variables form the basis for Nul A.
7. dim (Nul A) = number of free variables.

### Finding a Basis for the Column Space (Col A)
Col A = Span of the columns of A.
1. Row reduce A to find the pivot locations.
2. Identify which columns contain the pivots.
3. DANGER ZONE: Do NOT grab the columns from the RREF matrix itself. Row operations alter the column space!
4. Go back to the original matrix A and extract the columns corresponding to those pivot positions. These original columns form the basis for Col A.
5. dim (Col A) = number of pivot columns = Rank(A).

### The Rank Theorem
Rank(A) + dim (Nul A) = n
(where n is the total number of columns in matrix A)