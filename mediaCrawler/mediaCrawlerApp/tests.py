from django.test import TestCase
from .crawlerFunction.searchByKeyword import searchUserByKeyword, searchVideoByKeyword
from .models import TikTokUser, LiveStreamVideo, SimilarUser
from .repository import *
# Create your tests here.
class SearchByKeywordTest(TestCase):
    def test_search_user(self):
        searchUserByKeyword(3, "servo motor", True)

class TikTokUserTest(TestCase):
    # def test_add_tiktokUser_to_database(self):
    #     user = TikTokUser(name="John Doe", ip="192.168.1.1")
    #     user.save()

    #     all_users = TikTokUser.objects.all()
    #     self.assertTrue(len(all_users) == 1)
    #     self.assertTrue(all_users[0].name == "John Doe")
    
    # def test_remove_tiktokUser_from_database(self):
    #     user = TikTokUser(name="John Doe", ip="192.168.1.1")
    #     user.save()
        
    #     delete_user = TikTokUser.objects.get(mutable_id = user.mutable_id)
    #     delete_user.delete()

    #     all_users = TikTokUser.objects.all()
    #     self.assertTrue(len(all_users) == 0)

    # def test_update_tiktokUser_to_database(self):
    #     user = TikTokUser(name="John Doe", ip="192.168.1.1")
    #     user.save()

    #     update_user = TikTokUser.objects.get(mutable_id = user.mutable_id)
    #     update_user.name = "kai"
    #     update_user.save()

    #     all_users = TikTokUser.objects.all()
    #     self.assertTrue(len(all_users) == 1)
    #     self.assertTrue(all_users[0].name == "kai")

    # def test_scrape_tiktok_user_info(self):
    #     scrapeTikTokUsers("https://live.douyin.com/785392066244")
    #     all_users = TikTokUser.objects.all()
    #     users_string = ", ".join(str(user) for user in all_users)
    #     print("scrape_tik_tok_user_info result:")
    #     print(users_string)
    #     self.assertTrue(len(all_users) > 0)
        

    # def test_add_similarUser_to_tiktokUser(self):
    #     tiktok_user = TikTokUser(name="Test User", ip="192.168.1.1")
    #     tiktok_user.save()

    #     similar_user = SimilarUser(
    #         tiktok_user = tiktok_user,
    #         name="Similar User",
    #         url="https://example.com",
    #         ip="192.168.1.2"
    #     )
    #     similar_user.save()
    #     retrieved_similar_user = SimilarUser.objects.get(name="Similar User")
    #     self.assertEqual(retrieved_similar_user.tiktok_user, tiktok_user)
    
    # def test_get_tiktok_username (self):
    #     scrapeTikTokUsers("https://live.douyin.com/63592101250")
    #     all_user = TikTokUser.objects.all()
    #     print(all_user)
    #     self.assertTrue(len(all_user) > 0)
        
    def test_search_silmilar_users (self):
        user1 = TikTokUser(name="谢", ip="192.168.1.1", is_searched=False)
        user1.save()
        # User 2
        user2 = TikTokUser(name="承", ip="192.168.1.2", is_searched=False)
        user2.save()
        # User 3
        user3 = TikTokUser(name="君", ip="192.168.1.3", is_searched=False)
        user3.save()

        print(generateSimilarUsers())

    # def test_search_silmilar_users_multithread (self):
    #     scrapeTikTokUsers("https://live.douyin.com/374133902274")
    #     generate_similar_user_multithread(5)
    #     all_user = SimilarUser.objects.all()
    #     print(all_user)
    #     self.assertTrue(len(all_user) > 0)