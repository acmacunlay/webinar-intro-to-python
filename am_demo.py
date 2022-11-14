from time import sleep
from session_am.ram_utilization import RAMUtilization
from session_am import resource_monitor


def main(username: str) -> None:
    print("User: {}".format(username))
    monitor = resource_monitor.ResourceMonitor()

    while True:
        ram_info = RAMUtilization(
            ram_available=monitor.get_available_ram(),
            ram_percent=monitor.get_ram_utilization(),
        )
        print(ram_info)
        sleep(1)


if __name__ == "__main__":
    main("admin")
