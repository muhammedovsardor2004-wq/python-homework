#taks 1

import sqlite3 , pandas as pd

conn = sqlite3.connect('chinook.db')

customer = pd.read_sql('SELECT * FROM CUSTOMERS',conn)
invoices = pd.read_sql('SELECT * FROM invoices',conn)

# har bor mijoz qancha sarflagani
customer_s = invoices.groupby('CustomerId').agg({'Total':'sum'})


top_5cust = (
    invoices.groupby('CustomerId')['Total']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
top_5cust


top_5cust_name = (
    invoices.groupby('CustomerId')['Total']
    .sum()
    .reset_index()
    .merge(
        customer[['CustomerId','FirstName','LastName']],
        on='CustomerId',
        how='left'
    )
    .sort_values("Total", ascending=False)
    .head(5)
)
top_5cust_name


#task 2

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)
invoice_items = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)
albums = pd.read_sql("SELECT AlbumId FROM albums", conn)


df = (
    invoice_items
    .merge(invoices, on="InvoiceId")
    .merge(tracks, on="TrackId")
)

df


album_track_counts = (
    tracks.groupby("AlbumId")
    .size()
    .reset_index(name="Total_Tracks_In_Album")
)
album_track_counts


customer_album_tracks = (
    df.groupby(["CustomerId", "AlbumId"])
    .size()
    .reset_index(name="Tracks_Purchased")
)
customer_album_tracks


customer_album_tracks = customer_album_tracks.merge(
    album_track_counts,
    on="AlbumId",
    how="left"
)

customer_album_tracks["Full_Album"] = (
    customer_album_tracks["Tracks_Purchased"]
    == customer_album_tracks["Total_Tracks_In_Album"]
)


customer_pref = (
    customer_album_tracks
    .groupby("CustomerId")["Full_Album"]
    .any()
    .reset_index()
)

customer_pref["Preference"] = customer_pref["Full_Album"].map(
    {True: "Full Album", False: "Individual Tracks"}
)


summary = (
    customer_pref["Preference"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
)

summary.columns = ["Purchase_Type", "Percentage"]
summary
