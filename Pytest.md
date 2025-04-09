# Pytest 中文课程笔记

## 11-1 测试框架定位和为什么学习 PyTest

### 什么是测试框架？

测试框架是为软件测试提供结构和支持的工具集合。它们旨在简化测试过程，提高测试效率和可维护性。测试框架通常包含以下组件：

- **测试用例组织和管理:** 框架提供结构化的方式来组织和管理测试用例，例如使用目录、文件或类来分组测试。
- **测试执行器:** 框架提供运行测试用例的机制，并收集测试结果。
- **断言库:** 框架提供断言函数或方法，用于验证实际结果与预期结果是否一致。
- **报告生成:** 框架可以生成测试报告，汇总测试结果，方便分析和跟踪问题。
- **辅助功能:** 一些框架还提供其他辅助功能，例如参数化测试、数据驱动测试、模拟对象、前后置操作等。

### 为什么学习 PyTest？

PyTest 是一个功能强大且易于使用的 Python 测试框架。它具有以下优点，使其成为学习和使用的理想选择：

- **简洁易学:** PyTest 的语法简洁直观，易于上手。即使是初学者也能快速编写和运行测试。
- **功能强大:** PyTest 提供了丰富的功能，包括自动测试发现、fixture、参数化、插件系统等，可以满足各种复杂的测试需求。
- **扩展性强:** PyTest 的插件系统非常强大，拥有大量的第三方插件，可以扩展其功能，例如生成漂亮的测试报告、进行性能测试、接口测试等。
- **良好的社区支持:** PyTest 拥有活跃的社区，文档完善，遇到问题容易找到解决方案。
- **兼容性好:** PyTest 可以与现有的 unittest 测试框架兼容，方便迁移和集成。

总而言之，PyTest 是一个现代、高效、灵活的 Python 测试框架，学习 PyTest 可以帮助您编写更高质量的测试代码，提高测试效率，并更好地保障软件质量。

## 11-2 unittest 框架及初识 Pytest（一）

### unittest 框架简介

unittest 是 Python 标准库中自带的测试框架，也被称为 PyUnit。它受到了 JUnit 的启发，提供了一套面向对象的测试框架。

**unittest 的核心概念：**

- **TestCase:** 测试用例，是测试的最小单元。在 unittest 中，测试用例通常是一个继承自 `unittest.TestCase` 的类，其中的每个测试方法都以 `test_` 开头。
- **TestSuite:** 测试套件，是测试用例的集合。可以将多个相关的测试用例组织到一个测试套件中。
- **TestRunner:** 测试运行器，用于执行测试套件中的测试用例，并生成测试结果。
- **Fixture:** 测试夹具，用于为测试用例准备测试环境和清理测试环境。unittest 使用 `setUp` 和 `tearDown` 方法来实现 fixture。
- **Assertion:** 断言，用于验证实际结果与预期结果是否一致。unittest 提供了丰富的断言方法，例如 `assertEqual`、`assertTrue`、`assertRaises` 等。

**unittest 的基本使用：**

```python
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 测试前的准备工作
        pass

    def tearDown(self):
        # 测试后的清理工作
        pass

    def test_something(self):
        self.assertEqual(1 + 1, 2)  # 断言 1+1 的结果是否等于 2

    def test_another_thing(self):
        self.assertTrue(True) # 断言 True 是否为真

if __name__ == '__main__':
    unittest.main()
```

### 初识 Pytest

Pytest 旨在简化测试编写，并提供更强大的功能。与 unittest 相比，Pytest 具有以下特点：

- **更简洁的语法:** Pytest 使用更简洁的语法，不需要继承 TestCase 类，也不需要编写 `setUp` 和 `tearDown` 方法（可以使用 fixture 替代）。
- **自动测试发现:** Pytest 可以自动发现测试文件和测试函数，无需手动组织测试套件。
- **丰富的断言:** Pytest 使用 Python 原生的 `assert` 语句进行断言，更加简洁直观。
- **强大的 fixture:** Pytest 的 fixture 功能非常强大，可以灵活地管理测试环境和数据。
- **插件系统:** Pytest 拥有丰富的插件，可以扩展其功能。

**Pytest 的基本使用：**

```python
# test_example.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2
```

**运行 Pytest 测试：**

在命令行中，进入测试文件所在的目录，运行 `pytest` 命令即可。Pytest 会自动发现并执行测试文件 `test_example.py` 中的测试函数。

## 11-3 unittest 框架及初识 Pytest（二）

### unittest 框架的更多用法

- **TestSuite 的使用:** 可以使用 `unittest.TestSuite` 类手动创建测试套件，并将多个测试用例添加到套件中。
- **TestRunner 的使用:** 可以使用不同的 TestRunner 来运行测试套件，例如 `unittest.TextTestRunner` (文本输出) 和 `unittest.HTMLTestRunner` (HTML 报告)。
- **跳过测试和预期失败:** 可以使用 `@unittest.skip` 装饰器跳过测试用例，使用 `@unittest.expectedFailure` 装饰器标记预期失败的测试用例。
- **参数化测试 (需要第三方库):** unittest 本身不直接支持参数化测试，但可以使用第三方库，例如 `ddt` 来实现参数化测试。

### Pytest 的更多特性

- **更灵活的测试发现:** Pytest 可以根据不同的命名约定和配置来发现测试文件和测试函数。
- **更强大的断言:** Pytest 除了可以使用 `assert` 语句外，还提供了一些辅助断言工具，例如 `pytest.raises` (用于断言异常)。
- **Fixture 的深入使用:** Pytest 的 fixture 可以实现更复杂的测试环境管理，例如 fixture 的作用域、自动使用 fixture、fixture 的参数化等。
- **标记 (Markers):** Pytest 可以使用标记 (markers) 对测试用例进行分类和分组，方便选择性执行测试。

**Pytest 标记示例：**

```python
import pytest

@pytest.mark.slow
def test_slow_function():
    # ... 耗时较长的测试 ...
    pass

@pytest.mark.fast
def test_fast_function():
    # ... 快速测试 ...
    pass
```

可以使用 `-m` 参数选择执行带有特定标记的测试用例，例如 `pytest -m slow` 只执行标记为 `slow` 的测试用例。

## 11-4 PyTest 的测试发现和配置

### Pytest 的测试发现规则

Pytest 默认的测试发现规则如下：

- **测试文件:** Pytest 会在当前目录及其子目录中查找以 `test_*.py` 或 `*_test.py` 命名的文件。
- **测试函数和测试类:** 在测试文件中，Pytest 会查找以下内容作为测试用例：
  - 以 `test_` 开头的函数。
  - 以 `Test` 开头的类，并且类中以 `test_` 开头的方法。

**自定义测试发现规则:**

可以通过 Pytest 的配置文件 `pytest.ini` 或 `pyproject.toml` 来自定义测试发现规则。例如，可以修改测试文件名的匹配模式，或者指定测试目录。

### Pytest 的配置

Pytest 的配置可以通过以下方式进行：

- **命令行选项:** 在运行 `pytest` 命令时，可以使用各种命令行选项来配置 Pytest 的行为，例如 `-v` (详细输出)、`-k` (关键字表达式过滤测试)、`-m` (标记表达式过滤测试) 等。
- **配置文件:** Pytest 可以读取配置文件 `pytest.ini`、`pyproject.toml` 或 `tox.ini` 来获取配置信息。配置文件可以设置默认的命令行选项、自定义测试发现规则、配置插件等。
- **环境变量:** Pytest 也可以读取环境变量来获取配置信息。

**常用的 Pytest 配置文件选项：**

- `testpaths`: 指定测试目录，可以指定多个目录。
- `python_files`: 指定测试文件名的匹配模式，默认为 `test_*.py *_test.py`。
- `python_classes`: 指定测试类名的匹配模式，默认为 `Test`。
- `python_functions`: 指定测试函数名的匹配模式，默认为 `test_`.
- `markers`: 注册自定义标记，可以提供标记的描述信息。
- `addopts`: 设置默认的命令行选项。

**`pytest.ini` 示例：**

```ini
[pytest]
testpaths = tests
python_files = check_*.py *_check.py
markers =
    slow: marks tests as slow to run
    fast: marks tests as fast to run
addopts = -v --cov=my_project --cov-report=html
```

## 11-5 Pytest 执行控制和前后置操作

### Pytest 的执行控制

- **选择测试用例:**
  - **文件名:** `pytest test_module.py` (执行单个文件)
  - **目录:** `pytest test_dir` (执行目录下的所有测试)
  - **关键字表达式 (-k):** `pytest -k "string"` (执行包含 "string" 的测试函数或类名)
  - **标记表达式 (-m):** `pytest -m "marker_name"` (执行带有 "marker_name" 标记的测试)
  - **节点 ID:** `pytest test_module.py::test_function` (执行特定文件中的特定函数)
- **停止模式:**
  - `-x` 或 `--maxfail=1`: 遇到第一个失败的测试用例就停止执行。
  - `--maxfail=n`: 遇到前 n 个失败的测试用例就停止执行。
- **并行执行:**
  - `pytest-xdist` 插件可以实现测试用例的并行执行，提高测试速度。

### Pytest 的前后置操作 (Fixture)

Pytest 使用 fixture 来管理测试的前后置操作，fixture 比 unittest 的 `setUp` 和 `tearDown` 更加灵活和强大。

**Fixture 的基本用法：**

- 使用 `@pytest.fixture` 装饰器定义 fixture 函数。
- fixture 函数的返回值可以被测试函数作为参数接收。
- fixture 函数可以使用 `yield` 语句来分隔 setup 和 teardown 代码。`yield` 之前的代码在测试函数执行前执行 (setup)，`yield` 之后的代码在测试函数执行后执行 (teardown)。

**Fixture 示例：**

```python
import pytest

@pytest.fixture()
def setup_data():
    print("\nSetup data...")
    data = [1, 2, 3]
    yield data  # 返回数据给测试函数
    print("\nTeardown data...")

def test_use_fixture(setup_data):
    print("\nRunning test...")
    assert len(setup_data) == 3
```

**Fixture 的作用域 (scope):**

Fixture 可以设置不同的作用域，控制 fixture 的 setup 和 teardown 执行的频率：

- `function` (默认): 每个测试函数执行一次 setup 和 teardown。
- `class`: 每个测试类执行一次 setup 和 teardown。
- `module`: 每个模块 (文件) 执行一次 setup 和 teardown。
- `session`: 整个测试会话执行一次 setup 和 teardown。

**设置 fixture 作用域：**

```python
@pytest.fixture(scope="module")
def module_fixture():
    print("\nModule fixture setup...")
    yield
    print("\nModule fixture teardown...")
```

## 11-6 强大的 fixture

### Fixture 的参数化

Fixture 可以通过 `params` 参数实现参数化，让 fixture 返回不同的值，从而让测试函数在不同的参数下运行。

**Fixture 参数化示例：**

```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def param_fixture(request):
    return request.param

def test_param_fixture(param_fixture):
    print(f"\nRunning test with param: {param_fixture}")
    assert param_fixture > 0
```

`request` fixture 是 Pytest 内置的 fixture，可以访问当前测试请求的信息，包括参数化参数 `request.param`。

### Fixture 的自动使用 (autouse)

可以使用 `autouse=True` 参数让 fixture 自动在所有测试函数中被使用，无需显式地作为参数传递。

**自动使用 fixture 示例：**

```python
import pytest

@pytest.fixture(autouse=True)
def autouse_fixture():
    print("\nAutouse fixture setup and teardown...")
    yield

def test_function_1():
    print("\nTest function 1...")
    assert True

def test_function_2():
    print("\nTest function 2...")
    assert True
```

`autouse_fixture` 会在 `test_function_1` 和 `test_function_2` 执行前后自动执行 setup 和 teardown 代码。

### Fixture 的组合和依赖

Fixture 可以相互依赖和组合使用，一个 fixture 可以使用其他 fixture 的返回值作为参数。

**Fixture 组合和依赖示例：**

```python
import pytest

@pytest.fixture()
def db_connection():
    print("\nConnecting to database...")
    conn = ... # 建立数据库连接
    yield conn
    print("\nClosing database connection...")
    conn.close()

@pytest.fixture()
def user_data(db_connection): # 依赖 db_connection fixture
    print("\nFetching user data from database...")
    user = db_connection.query("SELECT * FROM users WHERE id = 1")
    yield user

def test_use_user_data(user_data): # 使用 user_data fixture
    print("\nRunning test with user data...")
    assert user_data is not None
```

`user_data` fixture 依赖 `db_connection` fixture，Pytest 会先执行 `db_connection` fixture 的 setup 代码，再执行 `user_data` fixture 的 setup 代码，然后执行 `test_use_user_data` 测试函数，最后依次执行 `user_data` 和 `db_connection` fixture 的 teardown 代码。

## 11-7 pytest 参数化和数据驱动

### Pytest 参数化 (@pytest.mark.parametrize)

`@pytest.mark.parametrize` 装饰器可以实现测试函数的参数化，让一个测试函数在不同的参数下运行多次。

**参数化示例：**

```python
import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (3, 4), (5, 6)])
def test_addition_parametrize(input, expected):
    assert input + 1 == expected
```

`@pytest.mark.parametrize("input, expected", [(1, 2), (3, 4), (5, 6)])` 表示测试函数 `test_addition_parametrize` 将会运行三次，每次 `input` 和 `expected` 的值分别为 `(1, 2)`、`(3, 4)`、`(5, 6)`。

### 数据驱动测试

参数化测试是实现数据驱动测试的基础。数据驱动测试是指测试用例的输入数据和预期结果都来自外部数据源，例如 CSV 文件、Excel 文件、数据库等。

**从 CSV 文件读取数据进行参数化测试示例：**

```python
import pytest
import csv

def read_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # 跳过表头
        for row in reader:
            data.append((int(row[0]), int(row[1])))
    return data

test_data = read_data_from_csv("test_data.csv")

@pytest.mark.parametrize("input, expected", test_data)
def test_addition_data_driven(input, expected):
    assert input + 1 == expected
```

**`test_data.csv` 文件内容：**

```csv
input,expected
1,2
3,4
5,6
```

## 11-8 pytest-mock 插件进行对象模拟

### 什么是对象模拟 (Mocking)？

对象模拟 (Mocking) 是一种测试技术，用于在测试过程中替换掉被测代码依赖的外部组件或对象，以便隔离被测代码，专注于测试其自身逻辑。

**对象模拟的应用场景：**

- **隔离外部依赖:** 当被测代码依赖于外部服务 (例如数据库、API、文件系统) 时，可以使用 Mock 对象来模拟这些外部依赖，避免测试受到外部环境的影响。
- **模拟复杂行为:** 可以使用 Mock 对象来模拟外部组件的复杂行为，例如异常抛出、特定返回值等，以便测试被测代码在各种情况下的处理逻辑。
- **提高测试速度:** Mock 对象通常比真实对象更快，使用 Mock 对象可以提高测试速度。

### pytest-mock 插件

`pytest-mock` 是一个 Pytest 插件，提供了方便的 Mock 功能。它基于 `unittest.mock` 库，并提供了 Pytest fixture `mocker` 来创建和管理 Mock 对象。

**pytest-mock 的基本使用：**

- 在测试函数中，将 `mocker` fixture 作为参数接收。
- 使用 `mocker.patch()` 方法来替换对象或函数。
- 使用 Mock 对象的方法 (例如 `return_value`、`side_effect`、`call_count`、`assert_called_with`) 来设置 Mock 对象的行为和断言 Mock 对象的调用情况。

**pytest-mock 示例：**

```python
import pytest
import requests

def get_user_name(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status() # 检查请求是否成功
    user_data = response.json()
    return user_data["name"]

def test_get_user_name(mocker):
    # 模拟 requests.get 方法
    mock_get = mocker.patch("requests.get")
    # 设置 Mock 对象的返回值
    mock_get.return_value.json.return_value = {"name": "John Doe"}

    user_name = get_user_name(123)
    assert user_name == "John Doe"
    # 断言 requests.get 方法被调用了一次，并且参数为 "https://api.example.com/users/123"
    mock_get.assert_called_once_with("https://api.example.com/users/123")
```

## 11-9 pytest 结合 Allure 生成高颜值报告

### Allure 报告简介

Allure 是一款开源的测试报告框架，可以生成美观、详细、可定制的测试报告。Allure 报告支持多种测试框架，包括 Pytest、JUnit、TestNG 等。

**Allure 报告的特点：**

- **美观的界面:** Allure 报告界面简洁美观，易于阅读和分析。
- **详细的测试信息:** Allure 报告可以展示测试用例的详细信息，包括步骤、附件、日志、参数等。
- **可定制性强:** Allure 报告可以根据需要进行定制，例如添加自定义信息、修改报告样式等。
- **支持多种格式:** Allure 报告可以生成多种格式的报告，例如 HTML、XML、JSON 等。

### pytest-allure 插件

`pytest-allure` 是一个 Pytest 插件，用于将 Pytest 测试结果集成到 Allure 报告中。

**pytest-allure 的基本使用：**

1.  **安装 `pytest-allure` 插件:** `pip install pytest-allure-adaptor`
2.  **运行 Pytest 测试时，添加 `--alluredir` 选项，指定 Allure 报告数据存储目录:** `pytest --alluredir=allure-results`
3.  **使用 Allure 命令行工具生成 HTML 报告:** `allure generate allure-results -o allure-report --clean`

**Allure 报告常用功能：**

- **测试步骤 (Steps):** 可以使用 `@allure.step` 装饰器定义测试步骤，在 Allure 报告中展示测试步骤的执行过程。
- **附件 (Attachments):** 可以使用 `allure.attach` 函数添加附件到 Allure 报告中，例如截图、日志文件、文本文件等。
- **特性 (Features) 和故事 (Stories):** 可以使用 `@allure.feature` 和 `@allure.story` 装饰器对测试用例进行分类，在 Allure 报告中进行分组展示。
- **严重程度 (Severity):** 可以使用 `@allure.severity` 装饰器设置测试用例的严重程度，在 Allure 报告中进行优先级排序。

**Allure 报告示例：**

```python
import pytest
import allure

@allure.feature("用户管理")
@allure.story("用户登录")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_login():
    with allure.step("输入用户名"):
        username = "testuser"
        allure.attach(username, "用户名", allure.attachment_type.TEXT)
    with allure.step("输入密码"):
        password = "password123"
        allure.attach(password, "密码", allure.attachment_type.TEXT)
    with allure.step("点击登录按钮"):
        pass
    with allure.step("验证登录成功"):
        assert True
```

## 11-10 Pytest 插件的 hook 机制（一）

## 11-11 Pytest 插件的 hook 机制（二）

### Pytest 插件简介

Pytest 插件是扩展 Pytest 功能的重要方式。Pytest 拥有强大的插件系统，允许开发者编写自定义插件来扩展 Pytest 的功能，例如：

- **修改测试发现规则**
- **自定义测试执行流程**
- **添加新的命令行选项**
- **生成自定义测试报告**
- **集成第三方工具**

Pytest 插件可以是：

- **内置插件:** Pytest 自带的一些插件，例如 `core` 插件、`capture` 插件、`runner` 插件等。
- **第三方插件:** 由社区开发的插件，可以通过 `pip install` 安装，例如 `pytest-xdist`、`pytest-cov`、`pytest-allure-adaptor` 等。
- **本地插件:** 用户在自己的项目中编写的插件，可以放在 `conftest.py` 文件中，或者作为独立的 Python 模块安装。

### Pytest 的 Hook 机制

Pytest 的 Hook 机制是插件系统的核心。Hook 是一种回调函数，Pytest 在执行测试过程中的特定阶段会调用这些 Hook 函数。插件可以通过实现 Hook 函数来干预 Pytest 的行为。

**Hook 函数的类型：**

Pytest 提供了大量的 Hook 函数，可以分为以下几类：

- **引导 Hook (Bootstrapping Hooks):** 在 Pytest 启动时调用的 Hook，例如 `pytest_load_initial_conftests`、`pytest_configure`。
- **收集 Hook (Collection Hooks):** 在测试收集阶段调用的 Hook，例如 `pytest_collect_file`、`pytest_generate_tests`。
- **运行 Hook (Test Running Hooks):** 在测试运行阶段调用的 Hook，例如 `pytest_runtest_setup`、`pytest_runtest_call`、`pytest_runtest_teardown`。
- **报告 Hook (Reporting Hooks):** 在测试报告生成阶段调用的 Hook，例如 `pytest_report_header`、`pytest_terminal_summary`。
- **错误处理 Hook (Error Handling Hooks):** 在测试过程中发生错误时调用的 Hook，例如 `pytest_exception_interact`、`pytest_internalerror`。

**Hook 函数的实现：**

- Hook 函数通常定义在 `conftest.py` 文件中，或者插件模块中。
- Hook 函数的命名必须遵循 `pytest_hookname` 的格式，例如 `pytest_configure`、`pytest_collection_modifyitems`。
- Hook 函数的参数由 Pytest 传递，参数类型和含义可以参考 Pytest 文档。

**Hook 函数的调用顺序：**

Pytest 会按照一定的顺序调用 Hook 函数，并且允许插件之间通过 Hook 函数进行交互。Hook 函数的调用顺序和优先级由 Pytest 内部机制管理。

**`conftest.py` 文件：**

`conftest.py` 是 Pytest 的本地插件配置文件，Pytest 会自动发现和加载 `conftest.py` 文件中的 Hook 函数和 fixture。

**`conftest.py` 示例：**

```python
# conftest.py

def pytest_configure(config):
    config.option.verbose = 2 # 设置默认的 verbose level 为 2

def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker("slow") # 为所有测试用例添加 "slow" 标记
```

## 11-12 PyTest -- 本章总结

### Pytest 总结

Pytest 是一个功能强大、易于使用、扩展性强的 Python 测试框架。它具有以下核心特性：

- **简洁的语法和易用性:** Pytest 使用简洁的语法，易于学习和使用，可以快速编写和运行测试。
- **自动测试发现:** Pytest 可以自动发现测试文件和测试函数，无需手动组织测试套件。
- **强大的 fixture 系统:** Pytest 的 fixture 功能非常强大，可以灵活地管理测试环境和数据，实现参数化、作用域控制、自动使用、组合和依赖等高级功能。
- **参数化和数据驱动测试:** Pytest 提供了 `@pytest.mark.parametrize` 装饰器，方便实现参数化和数据驱动测试。
- **丰富的插件系统:** Pytest 拥有强大的插件系统，可以通过插件扩展其功能，例如生成漂亮的测试报告、进行对象模拟、并行执行测试等。
- **Hook 机制:** Pytest 的 Hook 机制允许插件干预 Pytest 的行为，实现高度定制化的测试框架。

### 学习 Pytest 的价值

学习 Pytest 可以为您带来以下价值：

- **提高测试效率:** Pytest 的简洁语法、自动测试发现、强大的 fixture 系统可以大大提高测试编写和执行效率。
- **提高测试代码质量:** Pytest 鼓励编写清晰、可读、可维护的测试代码。
- **更好地保障软件质量:** 通过使用 Pytest 进行全面的测试，可以更有效地发现和预防软件缺陷，提高软件质量。
- **提升职业竞争力:** Pytest 是 Python 测试领域最流行的框架之一，掌握 Pytest 可以提升您的技术能力和职业竞争力。

希望这份笔记能够帮助您系统地学习 Pytest 框架。祝您学习愉快！
