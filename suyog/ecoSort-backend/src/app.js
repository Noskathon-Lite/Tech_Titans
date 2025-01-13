import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
// import router from "./router/user.route.js";
// import  passport  from "./middleware/passport.js";
// import session from 'express-session';
// import { swaggerUi, swaggerDocs} from './swagger.js'; 

const app=express();


app.use(cors(
    {
        origin:process.env.CORS_ORIGIN,
         credentials:true
    }
))

app.use(express.json({limit:"16kb"}))
app.use(express.urlencoded({extended:true,limit:"16kb"}))
app.use(express.static("public"))
app.use(cookieParser())

// app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));




// app.use(session({
//     secret: process.env.SESSION_SECRET || '1234', 
//     resave: false, 
//     saveUninitialized: false, 
//     cookie: { secure: false } 
//   }));
  

// app.use(passport.initialize());
// app.use(passport.session());

// app.use("/api/v1/users",router)



export default app
