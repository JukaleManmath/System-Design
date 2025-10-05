# System Design Patterns Repository

Welcome to the **System-Design** repository! This project aims to provide a comprehensive collection of system design patterns, each accompanied by core code structures and real-life example code. The goal is to make it easy to understand, implement, and apply these patterns in practical scenarios.

## Repository Structure

- Each design pattern will have:
  - **Core Code:** The minimal, essential implementation of the pattern.
  - **Real-Life Example:** A practical scenario demonstrating how the pattern can be used.

## Patterns Included

### 1. Singleton Pattern
- **Description:** Ensures a class has only one instance and provides a global point of access to it.
- **Files:**  
  - `singleton_core.py` (Core implementation)
  - `singleton_example.py` (Real-life example)

#### Example Usage
```python
# singleton_example.py
from singleton_core import Singleton

class Logger(Singleton):
    def log(self, message):
        print(f"LOG: {message}")

logger1 = Logger()
logger2 = Logger()
assert logger1 is logger2  # Both are the same instance
logger1.log("Singleton works!")
```

---

## Coming Soon

Patterns planned for addition include (but are not limited to):
- Factory
- Builder
- Adapter
- Observer
- Strategy
- Proxy
- Decorator
- Facade
- Command

If you have suggestions for other patterns or real-life scenarios, feel free to open an issue or submit a pull request!

---

## Contributing

Contributions are welcome! If you'd like to add a new pattern, improve documentation, or provide additional real-life examples, please:
1. Fork the repository.
2. Add your changes.
3. Submit a pull request.

Check out the [issues](https://github.com/JukaleManmath/System-Design/issues) page for ideas or to report bugs.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

For questions or feedback, open an issue or contact the repository owner [@JukaleManmath](https://github.com/JukaleManmath).