import Home from "./pages/Home.vue";
import Posts from "./pages/Posts.vue";
import PostDetail from "./pages/PostDetail.vue";
import Projects from "./pages/Projects.vue";
import ProjectDetail from "./pages/ProjectDetail.vue";
import Tags from "./pages/Tags.vue";
import TagDetail from "./pages/TagDetail.vue";
import About from "./pages/About.vue";
import Contact from "./pages/Contact.vue";
import NotFound from "./pages/NotFound.vue";

const routes = [
  { path: "/", name: "home", component: Home },
  { path: "/posts", name: "posts", component: Posts },
  { path: "/posts/:slug", name: "post-detail", component: PostDetail },
  { path: "/projects", name: "projects", component: Projects },
  { path: "/projects/:slug", name: "project-detail", component: ProjectDetail },
  { path: "/tags", name: "tags", component: Tags },
  { path: "/tags/:tag", name: "tag-detail", component: TagDetail },
  { path: "/about", name: "about", component: About },
  { path: "/contact", name: "contact", component: Contact },
  { path: "/:pathMatch(.*)*", name: "not-found", component: NotFound }
];

export default routes;
