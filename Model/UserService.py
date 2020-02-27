from Model import User,Mentor,TrainingDetails

class UserService: 

    createProfile (User)
	viewMentor (Mentor.mentorId)
	searchMentor(Mentor.technology)
	selectMentor(Mentor.mentorId)
    sendProposal(User.userId, Mentor.mentorId)
    assignRating(TrainingDetails.rating)
    viewTrainings(TrainingDetails.status)