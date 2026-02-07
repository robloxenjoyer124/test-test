import dns.resolver

def get_dns_records(domain: str) -> dict:
    """
    Fetches DNS records for a domain.
    """
    records = {}
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]

    for r_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            records[r_type] = [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            records[r_type] = []
        except Exception as e:
            records[r_type] = [f"Error: {e}"]
    return records
