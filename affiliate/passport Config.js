const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const Affiliate = require('./affiliate/affiliateModel'); // Adjust the path if necessary

passport.use(new LocalStrategy(
  async (username, password, done) => {
    try {
      const user = await Affiliate.findOne({ username });
      if (!user) return done(null, false);
      // Verify password (you should hash passwords)
      // if (user.password !== password) return done(null, false);
      return done(null, user);
    } catch (error) {
      return done(error);
    }
  }
));

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser(async (id, done) => {
  try {
    const user = await Affiliate.findById(id);
    done(null, user);
  } catch (error) {
    done(error);
  }
});
