import typer
from rich import print
from rich.progress import track
from nexus_scan.modules.ip_lookup import get_ip_info
from nexus_scan.modules.dns_lookup import get_dns_records
from nexus_scan.modules.username import check_single_site, SITES
from nexus_scan.utils.display import (
    print_header, print_success, print_error,
    create_table, print_table, status_spinner, console
)

app = typer.Typer(help="NexusScan - Advanced OSINT Tool")

@app.command()
def ip(address: str):
    """
    Get geolocation and ISP info for an IP address.
    """
    print_header("IP Lookup", address)
    with status_spinner("Fetching IP info..."):
        data = get_ip_info(address)

    if data.get("status") == "fail":
        print_error(f"Failed: {data.get('message')}")
        return

    table = create_table("IP Information", ["Key", "Value"])
    for key, value in data.items():
        table.add_row(key, str(value))

    print_table(table)

@app.command()
def dns(domain: str):
    """
    Get DNS records for a domain.
    """
    print_header("DNS Lookup", domain)
    with status_spinner("Fetching DNS records..."):
        records = get_dns_records(domain)

    table = create_table("DNS Records", ["Type", "Values"])
    for r_type, values in records.items():
        if values:
            formatted_values = "\n".join(values)
            table.add_row(r_type, formatted_values)
        else:
            table.add_row(r_type, "[dim]No records found[/dim]")

    print_table(table)

@app.command()
def user(username: str):
    """
    Check for username existence on popular platforms.
    """
    print_header("Username Check", username)

    results = {}

    for site in track(SITES, description="Checking platforms..."):
        url_template = SITES[site]
        result = check_single_site(username, site, url_template)
        results[site] = result

    table = create_table("Social Media Profiles", ["Platform", "Status / URL"])

    found_count = 0
    for site, url in results.items():
        if url and url.startswith("http"):
            table.add_row(site, f"[link={url}]{url}[/link]")
            found_count += 1
        elif url is None:
             table.add_row(site, "[dim red]Not Found[/dim red]")
        else:
            table.add_row(site, f"[yellow]{url}[/yellow]")

    print_table(table)

    if found_count > 0:
        print_success(f"Found {found_count} profiles!")
    else:
        print_error("No profiles found.")

if __name__ == "__main__":
    app()
