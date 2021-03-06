from chatbot.common.chat_share_data import ShareData
from chatbot.story.story_board_manager import StoryBoardManager

class DecisionMaker(ShareData):
    """
    (1) check intend is clear , if not return intend select list
    (2) check intend service type (story board, ontology and etc)
    """
    def run(self, share_data):
        """

        :param share_data:
        :return:
        """
        try :
            self.__dict__ = share_data.__dict__

            if ("타입" in share_data.get_story_slot_entity().keys()) :
                #If you attach Image you need to first Type "이미지"
                if (self.story_slot_entity["타입"] == "이미지"):
                    self.initialize_story()
                    share_data.set_intent_id("90")
                #Initialize
                elif (self.story_slot_entity["타입"] in ["안녕", "하이"]):
                    self.initialize_story()
                    share_data.set_output_data("포스코 AI봇입니다 무엇이 궁금한가요?")
                    share_data.__dict__ = self.__dict__
                    return share_data

                elif (self.story_slot_entity["타입"] in ["저장"]):
                    self.initialize_story()
                    share_data.set_output_data("현재까지 대화 기록은 모델 정합성 향상에 사용됩니다")
                    share_data.__dict__ = self.__dict__
                    return share_data
            #Story Exist
            if (self.story_board_id != "") :
                share_data = StoryBoardManager("cb0007", self.story_board_id).run(share_data)
            #First Story
            else :
                share_data = self._get_story_board(share_data)
            share_data.__dict__ = self.__dict__
            return share_data

        except Exception as e:
            raise Exception(e)

    def _get_story_board(self, share_data) :
        try :
            # TODO: temp logic will be move to decistion maker
            # if(share_data.get_request_type() == 'image') :
            #     share_data.set_intent_id('1')

            # TODO : Intent and Story ID is in DB
            if(self.intent_id == "1") :
                share_data.set_story_id("1")
                share_data.set_service_type("find_image")
                share_data.set_output_data("이미지를 첨부하세요")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
            elif(self.intent_id == "2") :
                share_data.set_story_id("2")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_info")
            elif(self.intent_id == "3") :
                share_data.set_story_id("3")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_leader")
            elif(self.intent_id == "4") :
                share_data.set_story_id("4")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_biz")
            elif(self.intent_id == "5") :
                share_data.set_story_id("5")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_AI_member")
            elif(self.intent_id == "6") :
                share_data.set_story_id("6")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_leader")
            elif(self.intent_id == "7") :
                share_data.set_story_id("7")
                StoryBoardManager("cb0007",share_data.get_story_id()).run(share_data)
                share_data.set_service_type("find_meeting")
            #Set Image Parameter
            elif(self.intent_id == "90") :
                share_data.set_intent_id("1")
                share_data.set_story_id("1")
                share_data.set_service_type("find_image")
                share_data.set_output_data("이미지를 첨부하세요")
            else :
                share_data.set_story_id("99")
                share_data.set_output_data("무슨 말씀인지 잘 모르겠어요")
            return share_data
        except Exception as e:
            raise Exception(e)