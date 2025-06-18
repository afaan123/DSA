# Data Structures and Algorithms (DSA) in Python

A comprehensive learning repository for mastering Data Structures and Algorithms using Python. This repository contains organized study materials, practice problems, and implementations of various DSA concepts.

## Repository Structure

### Python Fundamentals
Complete Python programming course covering:
- **Basic Data Types & Variables** - Numbers, strings, booleans, and variable concepts
- **Control Flow** - if/else statements, loops, and conditional execution
- **Data Structures** - Lists, tuples, dictionaries, sets, and strings
- **Functions** - Custom functions, lambda functions, decorators, and higher-order functions
- **Object-Oriented Programming** - Classes, inheritance, and special methods
- **File Handling** - Reading/writing text files, CSV processing
- **Libraries** - NumPy, Pandas, Matplotlib, and third-party modules
- **Advanced Topics** - Generators, comprehensions, exceptions, and more

### 🔢 Array & Hashing Problems
LeetCode-style problems with multiple solution approaches:

#### Contains Duplicates
- `bruteforce.py` - O(n²) time complexity approach
- `hashset.py` - O(n) time complexity using hash set
- `sorting.py` - O(n log n) time complexity using sorting

#### Two Sums
- `bruteforce.py` - O(n²) time complexity approach
- `hashmap.py` - O(n) time complexity using hash map
- `sorting.py` - O(n log n) time complexity using sorting

#### Valid Anagrams
- `counter.py` - Using Python's Counter class
- `hashmap.py` - Manual hash map implementation
- `hashtable.py` - Alternative hash table approach

### 📝 Practice Notebooks
- `functions.ipynb` - Function implementation practice
- `inbuiltds.ipynb` - Built-in data structures exploration
- `blind.ipynb` - Blind coding practice problems
- `patterns.ipynb` - Common programming patterns

### 🎯 Additional Learning Materials
- `4.4-Mapsfunction.ipynb` - Map function tutorials and examples
- `4.5-filterfunction.ipynb` - Filter function tutorials and examples
- Various Jupyter notebooks for hands-on learning

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook (for interactive learning)
- Basic understanding of programming concepts

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd DSA

# Install required packages (if any)
pip install -r requirements.txt

# Start Jupyter Notebook
jupyter notebook
```

## 📖 Learning Path

### 1. Python Fundamentals (Recommended First)
Start with the `python-fundamentals/` directory:
1. **03 - Python Basics** - Core concepts
2. **04 - Conditional Execution** - Control flow
3. **05 - Sequence Types** - Lists, tuples, strings
4. **13 - Functions** - Function fundamentals
5. **08 - Dictionaries** - Key-value data structures
6. **09 - Sets** - Unique element collections

### 2. Advanced Python Concepts
Continue with:
- **10 - Comprehensions** - List, dict, and set comprehensions
- **16 - Higher Order Functions** - Functions as first-class citizens
- **18 - Decorators** - Function decorators and patterns
- **26 - Custom Classes** - Object-oriented programming

### 3. Data Science Libraries
Explore data manipulation and visualization:
- **29 - NumPy** - Numerical computing
- **30 - Pandas** - Data analysis and manipulation
- **31 - Matplotlib** - Data visualization

### 4. DSA Problems
Practice with the `Array_&_Hashing/` problems:
1. Start with **Contains Duplicates** - Basic array manipulation
2. Move to **Two Sums** - Hash map applications
3. Practice **Valid Anagrams** - String manipulation

### 5. Practice and Reinforcement
Use the `practice/` directory for:
- Pattern recognition exercises
- Blind coding practice
- Function implementation drills

## 💡 Problem-Solving Approach

For each DSA problem, try to implement multiple solutions:

1. **Brute Force** - Start with the simplest approach
2. **Optimization** - Identify bottlenecks and improve
3. **Alternative Methods** - Explore different algorithms
4. **Time/Space Analysis** - Understand complexity trade-offs

## Testing Your Solutions

Each problem directory contains multiple solution files. Compare their performance:

```python
import time

# Test different approaches
start_time = time.time()
result = solution1(nums)
end_time = time.time()
print(f"Solution 1: {end_time - start_time:.6f} seconds")
```

## 📊 Progress Tracking

- Complete Python fundamentals sections
- Implement all solution approaches for each problem
- Practice with blind coding exercises
- Review and optimize solutions
- Document your learning insights

##  Contributing

Feel free to contribute by:
- Adding new problem solutions
- Improving existing implementations
- Adding more practice problems
- Enhancing documentation

## 📝 Notes

- Each solution includes time and space complexity analysis
- Multiple approaches are provided to understand trade-offs
- Jupyter notebooks include detailed explanations and examples
- Practice problems help reinforce concepts

## 🎯 Goals

- Master fundamental Python programming concepts
- Understand common data structures and their implementations
- Develop efficient problem-solving skills
- Build a strong foundation for technical interviews
- Gain practical experience with real-world coding challenges

---

**Happy Learning! 🚀**

*This repository is designed for self-paced learning. Take your time to understand each concept thoroughly before moving to the next.* 
