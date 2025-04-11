from src import imap_fetcher


# testing if imap fetcher is working
def test_imap_login():
    assert imap_fetcher.EMAIL is not None
    assert imap_fetcher.PASSWORD is not None
    assert imap_fetcher.status == "OK"
