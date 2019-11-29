# Test: Connect to MS SQL Server with pyodbc on macOS

## Preparation
### Install mssql-tools
```bash
$ brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
$ brew update
$ brew install mssql-tools
```

### Install pyodbc
```bash
$ pip install pyodbc
```

- [reference](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver15#macos)

## Test
### Start MS SQL Server
```bash
$ docker-compose up
```

- [reference](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash)

### Run pyodbc
```bash
$ python main.py
```

Done!
