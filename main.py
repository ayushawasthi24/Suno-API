import suno_wrapper

# Create the Suno client instance with the provided cookie
# client = suno_wrapper.Suno(
#     cookie="mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A193d34a749a1c93-0b3ef8448b88f8-26011851-144000-193d34a749a1c94%22%2C%22%24device_id%22%3A%20%22193d34a749a1c93-0b3ef8448b88f8-26011851-144000-193d34a749a1c94%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _gcl_au=1.1.184283415.1734416694; ajs_anonymous_id=ffdce44c-e4ec-4fa9-b50c-6ad4976119c9; _ga=GA1.1.1708152622.1734416694; _fbp=fb.1.1734416694340.78711635784170955; _tt_enable_cookie=1; _ttp=7Z3oMRs-gymEsyGxpg6c7MY0GYJ.tt.1; __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8ycUtnVEFGTUlXQ09Ta0lTNXdXbmdyWUdqSjEiLCJyb3RhdGluZ190b2tlbiI6ImFsZnNpaXQwNnJxY29scjk0bDJidHc1N2h6cGhzcWFxeDBqZjBvOTAifQ.oWVneH3rn2Nr1XWgeeRn4To_2yUk05E-EfLeybBfWh9bpPDSZWG2QaviU7HKKumsb7zxyqpjZPp4tz1RfoH0kZ_Gg5HZmXHjDL_lmioIe9aKS7Zp0pbwMbCVL1-Fh-TPixHB3cBDK3JRhbTrRAyrtucSkbXdMkIyLreP3YzChIcVAgFSvRhx13ZwRgGSYqc_xa94pjQK4u20xcZ3S_wuHNsy28kfO4-UESPN4LeulBetUF3Xc8YV5SKNT7in9lNTk0DmzXm_ENbyfNDS-nph4NlDb9zY9_CObM7pif_cw13X-LZgLZ-visxCIC8_gBaRrGSMkD9KaqOFdWnD-61l6g; __client_uat=1735845020; __client_uat_U9tcbTPE=1735845020; __cf_bm=tbaOmHwkJtxicyKoOj76r_w_x9q3Z.jp_UffcHvMnEo-1735890816-1.0.1.1-BEj0hF33CYbWfhJXbdumi7cee6Ef_H7UJFbaRjAOsXn7IBO2NHNYvlq8ryD.LeJ8wT8KOhnpKanG6FPagTApUw; _cfuvid=PcMUZX90pL0Bi5JpiVQffYvxwyt10YMi_vG6MTIDO2M-1735890816389-0.0.1.1-604800000; _ga_7B0KEDD7XP=GS1.1.1735890822.3.0.1735890822.0.0.0"
# )

client = suno_wrapper.Suno(
    cookie="_cfuvid=Ob80vRYB52mxUVXkcDtlebFjkNK_tHAdUQ2gBqLO_j4-1735893593742-0.0.1.1-604800000; ajs_anonymous_id=dcdf4bcb-5bb8-4466-ba44-1a01fba37eaa; __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8ycjZ5MDhxcEl6RkkzbG5NYzUzRlVNU09mSVciLCJyb3RhdGluZ190b2tlbiI6InpncHUzNnY2eWppbTA1ZGJ5M3hhYjdsc2FleHJ6bnJxZXN4OWc2MnYifQ.kZpxcunPdWj_w6_3QgVL65oc9DPHimna7AhlTh7rT2aq5gTCO6eg2qt2c33Uodwpw5aexlbgAtvx3nyK5lhWZ6SOZKwpbIAAFk9CIxsmrelrY6uRualuL5tBOsixNTnObYgHyQdj3yOUF0tzRra3Gym3pCiER1jqz6a-mPNDKipiqOVVi3KrHlgdpW4TpFOCHwkIagPQ4mwe-ijKhWo7Lyj5pH9dsP3uPHAEjL5DOI_qhlRb0nFfR-g074fzqsMxCl_2uf7dUinDIm0uMuYlKP7aWJ2Y-nYiV9J71xmSIy3i3h3v4LgEK00H8tViL5AMjF63fkSGBxsw2b2AN6URHw; __client_uat=1735893615; __client_uat_U9tcbTPE=1735893615; __cf_bm=vf84oPXeAtvLUvR7QUS9CUnbND_mFFnCqwkf6ywg2eg-1735896388-1.0.1.1-jU4l0TJ3ra7WIUKP8AoeQExe4J4Q.cKHM3fwAHyDYkCBQ6jprcMaUlmOXsRtMpi.T6NLW4gAtGOfce4grIplUw"
)

clips = client.generate_song("", instrumental=False)
print(clips)

songs = client.get_songs()

urls = [song.get("audio_url") for song in songs[:2]]

for url in urls:
    print(url)
