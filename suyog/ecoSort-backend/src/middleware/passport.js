import passport from 'passport';
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
import userModel from '../models/user.model.js'; 



// Google OAuth strategy configuration
passport.use(new GoogleStrategy({

  clientID: process.env.GOOGLE_CLIENT_ID||"571770307244-d81faed01ricres76nhcp751bn5a19d3.apps.googleusercontent.com",
  clientSecret: process.env.GOOGLE_CLIENT_SECRET||"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",  
  callbackURL: "/api/v1/users/auth/google/callback" 
},
async (accessToken, refreshToken, profile, done) => {
  try {
    let user = await userModel.findOne({ googleId: profile.id });
    
    if (!user) {
      user = await userModel.create({
        googleId: profile.id,
        email: profile.emails[0].value, 
        username: profile.displayName,  
        profilePicture: profile.photos[0] ? profile.photos[0].value : null, 
      });
    }

    return done(null, user); 
  } catch (err) {
    return done(err, null); 
  }
}));


passport.serializeUser((user, done) => {
  done(null, user.id); 
});

passport.deserializeUser(async (id, done) => {
  try {
    const user = await userModel.findById(id);
    done(null, user); 
  } catch (err) {
    done(err, null); 
  }
});

export default passport; 